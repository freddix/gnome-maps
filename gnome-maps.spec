Summary:	Map viewer application for GNOME.
Name:		gnome-maps
Version:	3.14.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-maps/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	6a0f4573f6fc87ed01870f2ecb632b25
URL:		https://live.gnome.org/Design/Apps/Documents
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	glib-gio-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	clutter
Requires:	geocode-glib
Requires:	gjs
Requires:	hicolor-icon-theme
Requires:	libchamplain-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-maps

%description
Maps is a new map viewer application for GNOME. Based on collaborative
OpenStreetMap data, which is contributed to by hundreds of thousands
of people across the globe, it allows you to browse street maps and
satellite images. Maps allows you to search for the names of towns,
cities and landmarks, or for places of interest such as "cafes near
Main Street, Boston" or "Hotels in New York".

%prep
%setup -q

# kill gnome common deps
%{__sed} -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/gnome-maps
%{_datadir}/dbus-1/services/org.gnome.Maps.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-maps
%{_desktopdir}/org.gnome.Maps.desktop
%{_iconsdir}/hicolor/*/*/*.png

