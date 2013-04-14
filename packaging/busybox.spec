Name:           busybox
Version:        1.20.2
Release:        0
License:        GPL-2.0+
Summary:        The Swiss Army Knife of Embedded Linux
Url:            http://www.busybox.net/
Group:          System/Base
Source:         http://busybox.net/downloads/%{name}-%{version}.tar.bz2
Source2:        busybox.tizen.config

%description
BusyBox combines tiny versions of many common UNIX utilities into a
small single executable. It provides minimalist replacements for most
of the utilities usually found in fileutils, shellutils, findutils,
textutils, grep, gzip, tar, and more. BusyBox provides a fairly
complete POSIX environment for any small or embedded system. The
utilities in BusyBox generally have fewer options than their
full-featured GNU cousins. The options that are included provide the
expected functionality and behave very much like their GNU
counterparts.

%prep
%setup -q
cp -a %{SOURCE2} .config

%build
export VERBOSE=-v
export BUILD_VERBOSE=2
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CC="gcc"
export HOSTCC=gcc
make -e oldconfig
make -e %{?_smp_mflags}
make -e doc busybox.links %{?_smp_mflags}

%install
install -d %{buildroot}%{_prefix}/bin
install -d %{buildroot}%{_datadir}/busybox
install busybox.links %{buildroot}%{_datadir}/busybox
install applets/install.sh %{buildroot}%{_bindir}/busybox.install
install busybox %{buildroot}%{_prefix}/bin

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/busybox
%{_bindir}/busybox.install
%dir %{_datadir}/busybox
%config %{_datadir}/busybox/busybox.links

%changelog
