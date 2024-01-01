# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-yarl
Epoch: 100
Version: 1.17.2
Release: 3%{?dist}
Summary: Python module to handle URLs
License: Apache-2.0
URL: https://github.com/aio-libs/yarl/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-expandvars
BuildRequires: python3-pip
BuildRequires: python3-setuptools >= 47
BuildRequires: python3-tomli

%description
The module provides handy URL class for URL parsing and changing.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-yarl
Summary: Python module to handle URLs
Requires: python3
Requires: python3-idna >= 2.0
Requires: python3-multidict >= 4.0
Requires: python3-propcache >= 0.2.0
Provides: python3-yarl = %{epoch}:%{version}-%{release}
Provides: python3dist(yarl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-yarl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(yarl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-yarl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(yarl) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-yarl
The module provides handy URL class for URL parsing and changing.

%files -n python%{python3_version_nodots}-yarl
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-yarl
Summary: Python module to handle URLs
Requires: python3
Requires: python3-idna >= 2.0
Requires: python3-multidict >= 4.0
Requires: python3-propcache >= 0.2.0
Provides: python3-yarl = %{epoch}:%{version}-%{release}
Provides: python3dist(yarl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-yarl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(yarl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-yarl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(yarl) = %{epoch}:%{version}-%{release}

%description -n python3-yarl
The module provides handy URL class for URL parsing and changing.

%files -n python3-yarl
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
