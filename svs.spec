# TODO
# - needs samba sources to compile
Summary:	Samba Virus Scanner
Name:		svs
Version:	0.1.3
Release:	0.1
License:	GPL v3
Group:		Networking/Daemons
Source0:	http://downloads.sourceforge.net/svs/%{name}-%{version}.tar.bz2
# Source0-md5:
URL:		http://sourceforge.net/projects/svs/
BuildRequires:	QtCore-devel
BuildRequires:	QtTest-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Samba Virus Scanner (SVS) -- Samba VFS plugin for transparent and
parallel on-access virus scans.

%prep
%setup -qn %{name}

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES FAQ TODO README svs.ini.example
