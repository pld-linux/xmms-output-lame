Summary:	Mp3 output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS kompresuj�ca wyj�cie do plik�w mp3
Name:		xmms-output-lame
Version:	0.2.1
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	out_lame-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xmms-devel
BuildRequires:	lame-libs-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
This plugin allows xmms to play sounds though LAME mp3 encoder..

%description -l pl
Ta wtyczka pozwala xmms'owi odtwarza� muzyk� poprzez enkoder mp3 LAME..

%prep
%setup -q -n out_lame

%build
libtoolize -c -f
aclocal -I macros
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip README NEWS AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/Output/*
