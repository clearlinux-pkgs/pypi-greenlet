#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-greenlet
Version  : 1.1.2
Release  : 88
URL      : https://files.pythonhosted.org/packages/0c/10/754e21b5bea89d0e73f99d60c83754df7cc64db74f47d98ab187669ce341/greenlet-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0c/10/754e21b5bea89d0e73f99d60c83754df7cc64db74f47d98ab187669ce341/greenlet-1.1.2.tar.gz
Summary  : Lightweight in-process concurrent programming
Group    : Development/Tools
License  : MIT Python-2.0
Requires: pypi-greenlet-filemap = %{version}-%{release}
Requires: pypi-greenlet-lib = %{version}-%{release}
Requires: pypi-greenlet-license = %{version}-%{release}
Requires: pypi-greenlet-python = %{version}-%{release}
Requires: pypi-greenlet-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : python3-dev

%description
.. This file is included into docs/history.rst
.. image:: https://github.com/python-greenlet/greenlet/workflows/tests/badge.svg
:target: https://github.com/python-greenlet/greenlet/actions

%package dev
Summary: dev components for the pypi-greenlet package.
Group: Development
Requires: pypi-greenlet-lib = %{version}-%{release}
Provides: pypi-greenlet-devel = %{version}-%{release}
Requires: pypi-greenlet = %{version}-%{release}

%description dev
dev components for the pypi-greenlet package.


%package filemap
Summary: filemap components for the pypi-greenlet package.
Group: Default

%description filemap
filemap components for the pypi-greenlet package.


%package lib
Summary: lib components for the pypi-greenlet package.
Group: Libraries
Requires: pypi-greenlet-license = %{version}-%{release}
Requires: pypi-greenlet-filemap = %{version}-%{release}

%description lib
lib components for the pypi-greenlet package.


%package license
Summary: license components for the pypi-greenlet package.
Group: Default

%description license
license components for the pypi-greenlet package.


%package python
Summary: python components for the pypi-greenlet package.
Group: Default
Requires: pypi-greenlet-python3 = %{version}-%{release}

%description python
python components for the pypi-greenlet package.


%package python3
Summary: python3 components for the pypi-greenlet package.
Group: Default
Requires: pypi-greenlet-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(greenlet)

%description python3
python3 components for the pypi-greenlet package.


%prep
%setup -q -n greenlet-1.1.2
cd %{_builddir}/greenlet-1.1.2
pushd ..
cp -a greenlet-1.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656402537
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-greenlet
cp %{_builddir}/greenlet-1.1.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-greenlet/a0e4f5029d9a146a57a24b0c2a4615078bc1d759
cp %{_builddir}/greenlet-1.1.2/LICENSE.PSF %{buildroot}/usr/share/package-licenses/pypi-greenlet/c0710216ad228c4f1738a3212542f827d6fec097
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.10/greenlet/greenlet.h

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-greenlet

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-greenlet/a0e4f5029d9a146a57a24b0c2a4615078bc1d759
/usr/share/package-licenses/pypi-greenlet/c0710216ad228c4f1738a3212542f827d6fec097

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
