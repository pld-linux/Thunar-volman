%define		_realname	thunar-volman
Summary:	Volumes manager for Thunar
Summary(pl.UTF-8):	Menad¿er napêdów dla Thunara
Name:		Thunar-volman
Version:	0.1.2
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.berlios.de/xfce-goodies/%{_realname}-%{version}.tar.bz2
# Source0-md5:	910de35c398f70b66b38803bdfdd26f1
URL:		http://foo-projects.org/~benny/projects/thunar-volman/
BuildRequires:	Thunar-devel
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	gtk+2-devel >= 2.6
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	libexo >= 0.3.1.13
BuildRequires:	libtool
Requires:	Thunar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Thunar Volume Manager is an extension for the Thunar file manager,
which enables automatic management of removable drives and media. For
example, if thunar-volman is installed and configured properly, and
you plug in your digital camera, it will automatically launch your
preferred photo application and import the new pictures from the
camera into your photo collection.

%description -l pl.UTF-8
Thunar Volume Manager jest rozszerzeniem menad¿era plików Thunar,
które pozwala na automatyczne zarz±dzanie przeno¶nych dysków i mediów.
Dla przyk³adu, je¿eli thunar-volman jest zainstalowany i
skonfigurowany poprawnie i gydy pod³±czasz twój aparat cyfrowy,
thunar-volman automatycznie uruchomi preferowan± przez ciebie
aplikacjê i zaimportuje nowe zdjêcia z aparatu do twojej kolekcji
zdjêc.

%prep
%setup -q -n %{_realname}-%{version}

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

%files -f %{_realname}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/thunar-volman
%{_iconsdir}/*
