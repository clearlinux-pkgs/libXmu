#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libXmu
Version  : 1.1.2
Release  : 8
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXmu-1.1.2.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXmu-1.1.2.tar.gz
Summary  : Mini Xmu Library
Group    : Development/Tools
License  : MIT-Opengroup
Requires: libXmu-lib
Requires: libXmu-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xt)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xt)
BuildRequires : xmlto

%description
This library contains miscellaneous utilities and is not part of the Xlib
standard.  It contains routines which only use public interfaces so that it
may be layered on top of any proprietary implementation of Xlib or Xt.

%package dev
Summary: dev components for the libXmu package.
Group: Development
Requires: libXmu-lib
Provides: libXmu-devel

%description dev
dev components for the libXmu package.


%package dev32
Summary: dev32 components for the libXmu package.
Group: Default
Requires: libXmu-lib32

%description dev32
dev32 components for the libXmu package.


%package doc
Summary: doc components for the libXmu package.
Group: Documentation

%description doc
doc components for the libXmu package.


%package lib
Summary: lib components for the libXmu package.
Group: Libraries

%description lib
lib components for the libXmu package.


%package lib32
Summary: lib32 components for the libXmu package.
Group: Default

%description lib32
lib32 components for the libXmu package.


%prep
%setup -q -n libXmu-1.1.2
pushd ..
cp -a libXmu-1.1.2 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/Xmu/Atoms.h
/usr/include/X11/Xmu/CharSet.h
/usr/include/X11/Xmu/CloseHook.h
/usr/include/X11/Xmu/Converters.h
/usr/include/X11/Xmu/CurUtil.h
/usr/include/X11/Xmu/CvtCache.h
/usr/include/X11/Xmu/DisplayQue.h
/usr/include/X11/Xmu/Drawing.h
/usr/include/X11/Xmu/Editres.h
/usr/include/X11/Xmu/EditresP.h
/usr/include/X11/Xmu/Error.h
/usr/include/X11/Xmu/ExtAgent.h
/usr/include/X11/Xmu/Initer.h
/usr/include/X11/Xmu/Lookup.h
/usr/include/X11/Xmu/Misc.h
/usr/include/X11/Xmu/StdCmap.h
/usr/include/X11/Xmu/StdSel.h
/usr/include/X11/Xmu/SysUtil.h
/usr/include/X11/Xmu/WhitePoint.h
/usr/include/X11/Xmu/WidgetNode.h
/usr/include/X11/Xmu/WinUtil.h
/usr/include/X11/Xmu/Xct.h
/usr/include/X11/Xmu/Xmu.h
/usr/lib64/libXmu.so
/usr/lib64/libXmuu.so
/usr/lib64/pkgconfig/xmu.pc
/usr/lib64/pkgconfig/xmuu.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXmu.so
/usr/lib32/libXmuu.so
/usr/lib32/pkgconfig/32xmu.pc
/usr/lib32/pkgconfig/32xmuu.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libXmu/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXmu.so.6
/usr/lib64/libXmu.so.6.2.0
/usr/lib64/libXmuu.so.1
/usr/lib64/libXmuu.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXmu.so.6
/usr/lib32/libXmu.so.6.2.0
/usr/lib32/libXmuu.so.1
/usr/lib32/libXmuu.so.1.0.0
