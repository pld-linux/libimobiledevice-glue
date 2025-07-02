#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Common library for libimobiledevice and co.
Summary(pl.UTF-8):	Biblioteka wspólna dla libimobiledevice i pochodnych
Name:		libimobiledevice-glue
Version:	1.3.2
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://www.libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libimobiledevice-glue/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	742c66c3ce1f9ab4633b86c6daa343fd
URL:		https://libimobiledevice.org/
BuildRequires:	libplist-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Requires:	libplist >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library with common code used by the libraries and tools around the
libimobiledevice project.

%description -l pl.UTF-8
Biblioteka ze wspólnym kodem używanym przez biblioteki i narzędzia
wokół projektu libimobiledevice.

%package devel
Summary:	Header files for libimobiledevice-glue library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libimobiledevice-glue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libplist-devel >= 2.3.0

%description devel
Header files for libimobiledevice-glue library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libimobiledevice-glue.

%package static
Summary:	Static libimobiledevice-glue library
Summary(pl.UTF-8):	Statyczna biblioteka libimobiledevice-glue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libimobiledevice-glue library.

%description static -l pl.UTF-8
Statyczna biblioteka libimobiledevice-glue.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libimobiledevice-glue-1.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libimobiledevice-glue-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libimobiledevice-glue-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libimobiledevice-glue-1.0.so
%{_includedir}/libimobiledevice-glue
%{_pkgconfigdir}/libimobiledevice-glue-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libimobiledevice-glue-1.0.a
%endif
