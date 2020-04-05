
Summary: Embeddable, replicated and fault tolerant SQL engine
Name: dqlite
Version: 1.4.0
Release: 1%{?dist}
License: LGPLv3
URL: https://dqlite.io

Source0: https://github.com/canonical/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: sqlite-libs(wal-replication)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libuv)
BuildRequires: pkgconfig(raft)
BuildRequires: pkgconfig(libco)

Requires: sqlite-libs(wal-replication)

%description
dqlite is a C library that implements an embeddable and replicated
SQL database engine with high-availability and automatic failover.
The acronym "dqlite" stands for "distributed SQLite",
meaning that dqlite extends SQLite with a network protocol
that can connect together various instances of your application
and have them act as a highly-available cluster, with no dependency
on external databases.

%package devel
Summary: Development libraries for dqlite
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for dqlite

%prep
%setup -q

%build
autoreconf -i
%configure
%make_build

%install
make DESTDIR=${RPM_BUILD_ROOT} LIBDIR=%{_lib} install

%files
%{_libdir}/lib%{name}.so*
%exclude %{_libdir}/lib%{name}.a
%exclude %{_libdir}/lib%{name}.la

%files devel
%{_libdir}/pkgconfig/dqlite.pc
%{_includedir}/dqlite.h

%changelog
* Sun Apr 05 2020 Jan Pazdziora <adelton@fedoraproject.org> - 1.4.0-1
- Initial packaging.
