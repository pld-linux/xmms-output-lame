Summary:	MP3 output plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wyjściowa dla XMMS-a kompresująca wyjście do plików MP3
Name:		xmms-output-lame
Version:	0.2.2
Release:	3
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/my-xmms-plugs/out_lame-%{version}.tar.gz
# Source0-md5:	7ee5905e8eaa8eb149a9d6d260222abd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows XMMS to play sounds though LAME MP3 encoder.

%description -l pl.UTF-8
Ta wtyczka pozwala XMMS-owi odtwarzać muzykę poprzez koder MP3 LAME.

%prep
%setup -q -n out_lame

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_output_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root) %{xmms_output_plugindir}/*
