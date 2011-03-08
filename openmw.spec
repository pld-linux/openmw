#
# TODO: BRs, install files
#
Summary:	Morrowind reimplementation
Summary(pl.UTF-8):	Reimplementacja gry Morrowind
Name:		openmw
Version:	0.9.0
Release:	0.1
License:	GPL v3+
Group:		Applications/Emulators
Source0:	http://openmw.googlecode.com/files/%{name}-%{version}-source.tar.bz2
# Source0-md5:	025b2d88c8ed29d31590d75c0ead2bdd
Patch0:		%{name}-werror.patch
URL:		http://openmw.com/
BuildRequires:	cmake
BuildRequires:	libmpg123-devel
BuildRequires:	ogre-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenMW is an attempt to reimplement the popular role playing game
Morrowind. No game data is distributed with the code, the user must
already own a copy of Morrowind to use the software.

%description -l pl.UTF-8
OpenMW ma być w założeniu próbą reimplementacji popularnej gry RPG
Morrowind. Źródła nie zawierają plików danych, użytkownik musi
posiadać oryginalną kopię Morrowind jeżeli chce używać tego
oprogramowania.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a build/openmw $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/openmw
