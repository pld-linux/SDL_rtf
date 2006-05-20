Summary:	Simple DirectMedia Layer - RTF displaying
Summary(pl):	Biblioteka do wy¶wietlania dokumentów RTF pod SDL
Name:		SDL_rtf
Version:	0.1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_rtf/release/%{name}-%{version}.tar.gz
# Source0-md5:	fe36733167b5c89f128414f32612121a
URL:		http://www.libsdl.org/projects/SDL_rtf/
BuildRequires:	SDL-devel >= 1.2.5-2
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a sample library which allows you to display Rich Text Format
(RTF) documents in your SDL applications. It comes with an example
program "showrtf" which displays an RTF file using an SDL_ttf font
engine.

%description -l pl
Przyk³adowa biblioteka do wy¶wietlania dokumentów RTF (Rich Text
Format) w aplikacjach SDL. Pakiet zawiera przyk³adowy program
"showrtf", wy¶wietlaj±cy plik RTF przy u¿yciu silnika fontów SDL_ttf.

%package devel
Summary:	Header files and more to develop SDL_rtf applications
Summary(pl):	Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_rtf
Summary(pt_BR):	Cabeçalhos para desenvolver programas utilizando a %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.5-2

%description devel
Header files and more to develop SDL_rtf applications.

%description devel -l pl
Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_rtf.

%description devel -l pt_BR
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a %{name}.

%package static
Summary:	Static SDL_rtf libraries
Summary(pl):	Biblioteki statyczne SDL_rtf
Summary(pt_BR):	Biblioteca estática para desenvolvimento utilizando a %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_rtf libraries.

%description static -l pl
Biblioteki statyczne SDL_rtf.

%description static -l pt_BR
Este pacote contém a biblioteca estática que programadores vão
precisar para desenvolver aplicações linkados estaticamente com a
%{name}.

%prep
%setup -q

rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install .libs/showrtf $RPM_BUILD_ROOT%{_bindir}/showrtf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
