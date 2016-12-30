Summary:	VA-API implementation for Intel chipsets
Name:		libva-intel-driver
Version:	1.7.3
Release:	1
Group:		Video
License:	GPLv2+
Url:		http://cgit.freedesktop.org/vaapi/intel-driver/
Source0:	http://www.freedesktop.org/software/vaapi/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libva)
Obsoletes:	vaapi-driver-i965 < 1.0.15
%rename		vaapi-driver-intel

%description
libva-driver-intel is the VA-API implementation for Intel chipsets
and Intel HD Graphics for Intel Core processor family.

%files
%doc AUTHORS NEWS
%{_libdir}/dri/*_drv_video.so

#--------------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/dri/*.la
