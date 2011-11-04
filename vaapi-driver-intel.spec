%define name	vaapi-driver-intel
%define oname	intel-driver
%define version	1.0.15
%define rel	1

Summary:	VA-API driver for VDPAU interface
Name:		%{name}
Version:	%{version}
Release:	1
Group:		Video
License:	GPLv2+
URL:		http://cgit.freedesktop.org/vaapi/intel-driver/
Source:		http://cgit.freedesktop.org/vaapi/intel-driver/snapshot/%{oname}-%{version}.zip
BuildRequires:	libva-devel
Provides:	%{oname} = %{version}-%{release}

%description
VDPAU driver backend for VA API, a video acceleration API.

%prep
%setup -q -n %oname-%version
#% apply_patches

%build
autoreconf -v --install
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/dri/*.la

%files
%defattr(-,root,root)
%doc AUTHORS NEWS
%{_libdir}/dri/*_drv_video.so
