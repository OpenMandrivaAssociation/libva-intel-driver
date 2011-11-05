%define name	vaapi-driver-intel
%define oname	intel-driver
%define version	1.0.15
%define rel	1

Summary:	Is the VA-API implementation for Intel G45 chipsets
Name:		%{name}
Version:	%{version}
Release:	2
Group:		Video
License:	GPLv2+
URL:		http://cgit.freedesktop.org/vaapi/intel-driver/
Source:		http://cgit.freedesktop.org/vaapi/intel-driver/snapshot/%{oname}-%{version}.zip
BuildRequires:	libva-devel => 1.0.15
Provides:	%{oname} = %{version}-%{release}

%description
libva-driver-intel is the VA-API implementation for Intel G45 chipsets
and Intel HD Graphics for Intel Core processor family.


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
