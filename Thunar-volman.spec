%define		_realname	thunar-volman
Summary:	Volumes manager for Thunar
Summary(pl.UTF-8):	Zarządca napędów dla Thunara
Name:		Thunar-volman
Version:	0.3.80
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/thunar-volman/%{_realname}-%{version}.tar.bz2
# Source0-md5:	4fd81b62690797317ca649ab20609dae
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-volman
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	exo-devel >= 0.3.100
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	Thunar-devel >= 1.0.0
BuildRequires:	xfce4-dev-tools >= 4.6.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	Thunar >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Thunar Volume Manager is an extension for the Thunar file manager,
which enables automatic management of removable drives and media. For
example, if Thunar-volman is installed and configured properly, and
you plug in your digital camera, it will automatically launch your
preferred photo application and import the new pictures from the
camera into your photo collection.

%description -l pl.UTF-8
Thunar Volume Manager jest rozszerzeniem zarządcy plików Thunar,
które pozwala na automatyczne zarządzanie przenośnych dysków i mediów.
Na przykład, jeżeli Thunar-volman jest zainstalowany i skonfigurowany
poprawnie, przy podłączaniu aparatu cyfrowego automatycznie uruchomi
preferowaną aplikację i zaimportuje nowe zdjęcia z aparatu do kolekcji
zdjęć użytkownika.

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}

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
%attr(755,root,root) %{_libdir}/thunar-volman-settings
%{_desktopdir}/thunar-volman-settings.desktop
%{_iconsdir}/hicolor/*/apps/*
