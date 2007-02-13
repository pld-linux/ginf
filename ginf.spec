Summary:	GINF: Ginf Is Not FrontPage(TM)
Summary(pl.UTF-8):	Ginf Is Not FrontPage(TM) - narzędzie do tworzenia serwisów WWW
Name:		ginf
Version:	1.01
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.symonds.net/~deep/stuff/vtu/ginf/%{name}-%{version}-src.tar.gz
# Source0-md5:	c46e2897df52b780257397df2e75d444
Patch0:		%{name}-pixbuf.patch
URL:		http://www.symonds.net/~deep/stuff/vtu/ginf/index.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkhtml-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GINF is a Web-site creation software for the Linux platform, in the
lines of Netscape Composer and Microsoft FrontPage. You don't need to
know any HTML to create Web pages with GINF; instead you can just type
in the text and format it with the buttons and menus. GINF uses the
GTK+ widget set for the front-end, and the GtkHTML library for HTML
rendering.

%description -l pl.UTF-8
GINF to oprogramowanie do tworzenia serwisów WWW pod Linuksem w sposób
podobny do Netscape Composera i Microsoft FrontPage'a. Nie trzeba znać
języka HTML, aby tworzyć strony przy użyciu GINF-a; wystarczy pisać
tekst i formatować go przy pomocy przycisków i menu. GINF używa
zestawu widgetów GTK+ do interfejsu użytkownika i biblioteki GtkHTML
do wyświetlania HTML-a.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
touch po/POTFILES
rm -f missing acinclude.m4
rm -f install.sh
%{__libtoolize}
%{__gettextize} --intl
if [ -f po/Makevars.template ]; then
	cp po/Makevars.template po/Makevars
fi
%{__aclocal} -I macros
%{__autoheader}
%{__autoconf}
%{__automake}

#%%{__aclocal} -I m4
#%%{__automake} m4/Makefile

%configure \
	--without-included-gettext

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_pixmapsdir}/table $RPM_BUILD_ROOT%{_pixmapsdir}/ginf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
