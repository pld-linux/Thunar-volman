%define		_realname	thunar-volman
Summary:	Volumes manager for Thunar
Summary(pl.UTF-8):	Zarządca napędów dla Thunara
Name:		Thunar-volman
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{_realname}-%{version}.tar.bz2
# Source0-md5:	e4587967fe3b3858d93735fee3edb2fc
Patch0:		%{name}-locale-names.patch
URL:		http://foo-projects.org/~benny/projects/thunar-volman/
BuildRequires:	Thunar-devel >= 0.9.0
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	libexo-devel >= 0.3.4
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	startup-notification-devel
BuildRequires:	w3c-libwww-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	Thunar
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
%patch0 -p1

mv -f po/{nb_NO,nb}.po

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
