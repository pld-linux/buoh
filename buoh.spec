Summary:	The online comic reader application for GNOME
Summary(pl.UTF-8):	Czytników komiksów online dla GNOME
Name:		buoh
Version:	0.8.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://buoh.steve-o.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	5d05a51d7c6616d93e93df3465b49fe7
Patch0:		%{name}-desktop.patch
URL:		http://buoh.steve-o.org/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.7.0
BuildRequires:	intltool >= 0.11
BuildRequires:	libgnomeui-devel >= 2.6
BuildRequires:	libsoup-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/buoh64x64.png $RPM_BUILD_ROOT%{_pixmapsdir}/buoh.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install buoh.schemas

%preun
%gconf_schema_uninstall buoh.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_sysconfdir}/gconf/schemas/buoh.schemas
