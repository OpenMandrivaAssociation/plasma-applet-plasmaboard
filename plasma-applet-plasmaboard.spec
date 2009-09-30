Name:           plasma-applet-plasmaboard
Summary:        Plasmaboard is an On-screen keyboard for kde4
Version:        0.8
Release:        %mkrel 1
Url:            http://kde-look.org/content/show.php/Plasmaboard?content=101822
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://kde-look.org/CONTENT/content-files/101822-plasmaboard-0.5.tar.gz
BuildRequires:  plasma-devel
BuildRequires:  kdebase4-workspace-devel

%description
This is the first virtual keyboard for plasma.

%files
%defattr(-,root,root)
%doc README
%_kde_libdir/kde4/plasma_applet_plasmaboard.so
%_kde_datadir/kde4/services/plasma_applet_plasmaboard.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n plasmaboard

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot

