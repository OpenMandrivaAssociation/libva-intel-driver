Summary:	VA-API implementation for Intel chipsets
Name:		libva-intel-driver
Version:	1.8.0
Release:	1
Group:		Video
License:	GPLv2+
Url:		http://cgit.freedesktop.org/vaapi/intel-driver/
Source0:	https://github.com/01org/intel-vaapi-driver/releases/download/%{version}/intel-vaapi-driver-%{version}.tar.bz2
BuildRequires:	pkgconfig(libva)
Obsoletes:	vaapi-driver-i965 < 1.0.15
%rename		vaapi-driver-intel

%description
libva-driver-intel is the VA-API implementation for Intel chipsets
and Intel HD Graphics for Intel Core processor family.

%files
%{_libdir}/dri/*_drv_video.so

#--------------------------------------------------------------------------

%prep
%setup -qn intel-vaapi-driver-%{version}

%build
%configure
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/dri/*.la
rm -rf %{buildroot}%{_datadir}/
