Summary:	The online comic reader application for GNOME
Summary(pl.UTF-8):	Czytników komiksów online dla GNOME
Name:		buoh
Version:	0.8.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://buoh.steve-o.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	50474a8712ad20ab36d8f8058a4647fb
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-libsoup24.patch
URL:		http://buoh.steve-o.org/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Buoh is a reader for online strips comics. It is free software,
designed to work well under the GNOME Desktop.
Buoh has a number of features, including:
- select your favorites comic through a list of more than 130 comics,
- easy, simple an eye-candy view of an online comic,
- browsing over the comic strip archives,
- saving a comic to disk,
- integration with GNOME (respecting the lockdowns and HIG
  compliance).

%description -l pl.UTF-8
Buoh jest aplikacją umożliwiającą czytanie periodycznie umieszczanych
w sieci pasków z komiksami.
Buoh posiada wiele możliwości, między innymi:
- wybór preferowanych komiksów spośród ponad 130 dostępnych,
- łatwe i proste przeglądanie komiksu,
- przeglądanie archiwum komiksu,
- zapis komiksu na dysk,
- integrację ze środowiskiem GNOME.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install buoh.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall buoh.schemas

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/buoh
%{_datadir}/buoh
%{_desktopdir}/buoh.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_sysconfdir}/gconf/schemas/buoh.schemas
