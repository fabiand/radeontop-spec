%global commit 281462c0943486170ef7b2451d1c3c38268c3484
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout .20150215git%{shortcommit}

Summary:    View GPU utilization off AMD/ATI Radeon devices
Name:       radeontop
Version:    0.8
Release:    1%{?checkout}%{?dist}
License:    GPLv3
Group:      System Environment/Libraries
URL:        https://github.com/clbr/%{name}

Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: asciidoc gettext
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(pciaccess)
BuildRequires: pkgconfig(libdrm)

%description
RadeonTop shows the utilization of your GPU, both in general and by blocks.

Supported cards are R600 and up.


%prep
%setup -q -n %{name}-%{commit}


%build
# configure doesn't exist, but we need the exported CFLAGS and friends
%configure || :

# plain=1 prevents stripping
# CC="..." to also pass -g
# Upstream patch: https://github.com/clbr/radeontop/pull/8
make all %{?_smp_mflags} PREFIX=%{_prefix} plain=1 CC="gcc -g"


%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
%find_lang %{name}


%files -f %{name}.lang
%doc README.md TODO COPYING
%{_sbindir}/radeontop
%{_mandir}/man1/radeontop.1*


%changelog
* Sun Feb 15 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.8-1.git20150215.281462c
- Update to upstream 0.8

* Thu Apr 24 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-2.git20140421.eadc100
- Fix commit position, BuildRequirements, build, and man page inclusion (thanks mschwendt)

* Mon Apr 21 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-1.git20140421.eadc100
- Initial package
