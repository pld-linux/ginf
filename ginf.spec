Summary:	GINF: Ginf Is Not FrontPage(TM)
Summary(pl):	Ginf Is Not FrontPage(TM) - narzêdzie do tworzenia serwisów WWW
Name:		ginf
Version:	1.01
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.symonds.net/~deep/stuff/vtu/ginf/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-pixbuf.patch
URL:		http://www.symonds.net/~deep/stuff/vtu/ginf/index.php
BuildRequires:	gtk+-devel
BuildRequires:	gtkhtml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GINF is a Web-site creation software for the Linux platform, in the
lines of Netscape Composer and Microsoft FrontPage. You don't need to
know any HTML to create Web pages with GINF; instead you can just type
in the text and format it with the buttons and menus. GINF uses the
GTK+ widget set for the front-end, and the GtkHTML library for HTML
rendering.

%description -l pl
GINF to oprogramowanie do tworzenia serwisów WWW pod Linuksem w sposób
podobny do Netscape Composera i Microsoft FrontPage'a. Nie trzeba znaæ
jêzyka HTML, aby tworzyæ strony przy u¿yciu GINF-a; wystarczy pisaæ
tekst i formatowaæ go przy pomocy przycisków i menu. GINF u¿ywa
zestawu widgetów GTK+ do interfejsu u¿ytkownika i biblioteki GtkHTML
do wy¶wietlania HTML.

%prep
%setup -q -n %{name}
%patch0 -p1
cat <<EOF > fixpo
#!/bin/sh
cat po/Makevars.template po/Makefile > po/tmp
mv -f po/tmp po/Makefile
EOF
chmod u+rx fixpo

%build
touch po/POTFILES
rm -f missing acinclude.m4
rm -f install.sh
%{__libtoolize}
%{__gettextize} --intl
%{__aclocal} -I macros
autoheader
%{__autoconf}
%{__automake}

#%{__aclocal} -I m4
#%{__automake} m4/Makefile

%configure \
	--without-included-gettext

./fixpo

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
