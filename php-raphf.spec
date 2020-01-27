#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-raphf
Version  : 2.0.1
Release  : 3
URL      : https://pecl.php.net/get/raphf-2.0.1.tgz
Source0  : https://pecl.php.net/get/raphf-2.0.1.tgz
Summary  : A reusable split-off of pecl_http's persistent handle and resource factory API
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-raphf-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : util-linux

%description
# ext-raphf
[![Build Status](https://travis-ci.org/m6w6/ext-raphf.svg?branch=master)](https://travis-ci.org/m6w6/ext-raphf)

%package dev
Summary: dev components for the php-raphf package.
Group: Development
Requires: php-raphf-lib = %{version}-%{release}
Provides: php-raphf-devel = %{version}-%{release}
Requires: php-raphf = %{version}-%{release}
Requires: php-raphf = %{version}-%{release}

%description dev
dev components for the php-raphf package.


%package lib
Summary: lib components for the php-raphf package.
Group: Libraries

%description lib
lib components for the php-raphf package.


%prep
%setup -q -n raphf-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/raphf/php_raphf.h
/usr/include/php/ext/raphf/php_raphf_api.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/raphf.so
