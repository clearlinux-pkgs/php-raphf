#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-raphf
Version  : 2.0.1
Release  : 50
URL      : https://pecl.php.net/get/raphf-2.0.1.tgz
Source0  : https://pecl.php.net/get/raphf-2.0.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-raphf-lib = %{version}-%{release}
Requires: php-raphf-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# ext-raphf
[![Build Status](https://travis-ci.org/m6w6/ext-raphf.svg?branch=master)](https://travis-ci.org/m6w6/ext-raphf)

%package dev
Summary: dev components for the php-raphf package.
Group: Development
Requires: php-raphf-lib = %{version}-%{release}
Provides: php-raphf-devel = %{version}-%{release}
Requires: php-raphf = %{version}-%{release}

%description dev
dev components for the php-raphf package.


%package lib
Summary: lib components for the php-raphf package.
Group: Libraries
Requires: php-raphf-license = %{version}-%{release}

%description lib
lib components for the php-raphf package.


%package license
Summary: license components for the php-raphf package.
Group: Default

%description license
license components for the php-raphf package.


%prep
%setup -q -n raphf-2.0.1
cd %{_builddir}/raphf-2.0.1
pushd ..
cp -a raphf-2.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-raphf
cp %{_builddir}/raphf-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-raphf/d1612d99e29c3d2e8f9ccea2f877b1ba963a200b || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/raphf/php_raphf.h
/usr/include/php/ext/raphf/php_raphf_api.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/raphf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-raphf/d1612d99e29c3d2e8f9ccea2f877b1ba963a200b
