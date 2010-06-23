#
# TODO: BRs, install files
#
Summary:	Morrowind reimplementation
Summary(pl.UTF-8):	Reimplemantacja gry Morrowind
Name:		openmw
Version:	0.07
Release:	0.1
License:	GPL v3+
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/openmw/%{name}-%{version}.tar.bz2
# Source0-md5:	c40c80069c006b1e893fc74dcbefb3d9
URL:		http://openmw.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	ogre-devel
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
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install build/openmw $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/openmw