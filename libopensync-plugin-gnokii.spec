Name: 	 	libopensync-plugin-gnokii
Version: 	0.22
Release: 	%{mkrel 3}
Summary: 	Gnokii (Nokia) plugin for OpenSync synchronization framework
License:	GPLv2+
Group:		Office
URL:		http://www.opensync.org
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libopensync-plugin-gnokii-0.22-warning.patch
Obsoletes:	multisync-syncml
Provides:	multisync-syncml
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	gnokii-devel
Requires:	libopensync >= 1:%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise via
SyncML.

%prep
%setup -q
%patch0 -p1 -b .warning
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_libdir}/opensync/formats/*
%{_datadir}/opensync/defaults/*
