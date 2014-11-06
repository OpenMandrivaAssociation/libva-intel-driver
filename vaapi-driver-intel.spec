%define oname intel-driver

Summary:	Is the VA-API implementation for Intel G45 chipsets
Name:		vaapi-driver-intel
Version:	1.4.1
Release:	1
Group:		Video
License:	GPLv2+
Url:		http://cgit.freedesktop.org/vaapi/intel-driver/
Source0:	http://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-%{version}.tar.bz2
BuildRequires:	pkgconfig(libva) >= 0.35
Obsoletes:	vaapi-driver-i965 < 1.0.15

%description
libva-driver-intel is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.

%files
%doc AUTHORS NEWS
%{_libdir}/dri/*_drv_video.so

#--------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}

%build
autoreconf -v --install
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/dri/*.la
