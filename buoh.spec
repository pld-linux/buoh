# TODO:
# - adaptarize desktop file
# - choose better group
Summary:	The online comic reader application for GNOME
Summary(pl):	Czytników komiksów online dla GNOME
Name:		buoh
Version:	0.8
Release:	0.1
License:	GPLv2
Group:		X11/Applications/Networking
Source0:	http://buoh.steve-o.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	7c6042851e7db8ecaa2ca9cfe44f5c9c
URL:		http://buoh.steve-o.org/
BuildRequires:	gtk+2-devel >= 2.7
BuildRequires:	libsoup-devel >= 2.2
BuildRequires:	libgnomeui-devel >= 2.6
BuildRequires:	GConf2-devel >= 2.2
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

%description -l pl
Buoh jest aplikacj± umo¿liwiaj±c± czytanie periodycznie umieszczanych
w sieci pasków z komiksami.

Buoh posiada wiele mo¿liwo¶ci, miêdzy innymi:

- wybór preferowanych komiksów spo¶ród ponad 130 dostêpnych,
- ³atwe i proste przegl±danie komiksu,
- przegl±danie archiwum komiksu,
- zapis komiksu na dysk,
- integracjê ze ¶rodowiskiem GNOME.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_pixmapsdir}/
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}/pixmaps/buoh64x64.png $RPM_BUILD_ROOT/%{_pixmapsdir}/

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
