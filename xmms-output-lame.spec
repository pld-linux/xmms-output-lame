Summary:	Mp3 output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS kompresuj±ca wyj¶cie do plików mp3
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_output_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog
%attr(755,root,root) %{xmms_output_plugindir}/*
