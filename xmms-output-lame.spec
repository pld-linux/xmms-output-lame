Summary:	Mp3 output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS kompresuj±ca wyj¶cie do plików mp3
Name:		xmms-output-lame
Version:	0.2.1
Release:	4
License:	GPL
Group:		Development/Libraries
Source0:	http://prdownloads.sourceforge.net/my-xmms-plugs/out_lame-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmms_plugin_dir	%(xmms-config --output-plugin-dir)

%description 
This plugin allows xmms to play sounds though LAME mp3 encoder.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê poprzez koder mp3 LAME.

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root)  %{_xmms_plugin_dir}/*
