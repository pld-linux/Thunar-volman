%define		_realname	thunar-volman
Summary:	Volumes manager for Thunar
Summary(pl.UTF-8):	Zarządca napędów dla Thunara
Name:		Thunar-volman
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/thunar-volman/0.9/%{_realname}-%{version}.tar.bz2
# Source0-md5:	4992a18f422918c33b562d6e66045754
Patch0:		%{name}-desktop.patch
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-volman
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gtk+3-devel
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libxfce4ui-devel >= 4.12.0
BuildRequires:	libxfce4util-devel >= 4.12.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	udev-glib-devel >= 145
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfconf-devel >= 4.12.0
Requires:	gtk-update-icon-cache
Requires:	gvfs
Requires:	hicolor-icon-theme
Requires:	Thunar >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Thunar Volume Manager is an extension for the Thunar file manager,
which enables automatic management of removable drives and media. For
example, if Thunar-volman is installed and configured properly, and
you plug in your digital camera, it will automatically launch your
preferred photo application and import the new pictures from the
camera into your photo collection.

%description -l pl.UTF-8
Thunar Volume Manager jest rozszerzeniem zarządcy plików Thunar, które
pozwala na automatyczne zarządzanie przenośnych dysków i mediów. Na
przykład, jeżeli Thunar-volman jest zainstalowany i skonfigurowany
poprawnie, przy podłączaniu aparatu cyfrowego automatycznie uruchomi
preferowaną aplikację i zaimportuje nowe zdjęcia z aparatu do kolekcji
zdjęć użytkownika.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{_realname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/thunar-volman
%attr(755,root,root) %{_bindir}/thunar-volman-settings
%{_desktopdir}/thunar-volman-settings.desktop
%{_iconsdir}/hicolor/*/apps/*
