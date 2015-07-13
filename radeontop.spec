%global commit0 281462c0943486170ef7b2451d1c3c38268c3484
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global checkout .20150215git%{shortcommit0}

Summary:    View GPU utilization of AMD/ATI Radeon devices
Name:       radeontop
Version:    0.8
Release:    2%{?checkout}%{?dist}
License:    GPLv3
URL:        https://github.com/clbr/%{name}

Source0:    %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: asciidoc gettext
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(pciaccess)
BuildRequires: pkgconfig(libdrm)

%description
RadeonTop shows the utilization of your GPU, both in general and by blocks.

Supported cards are R600 and up.


%prep
%setup -qn %{name}-%{commit0}


%build
# configure doesn't exist, but we need the exported CFLAGS and friends
%configure || :

sed -i "s/install: all/install:/" Makefile

# plain=1 prevents stripping
# CC="..." to also pass -g
# Upstream patch: https://github.com/clbr/radeontop/pull/8
make all %{?_smp_mflags} PREFIX=%{_prefix} plain=1 CC="gcc -g"


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc README.md TODO
%{_sbindir}/radeontop
%{_mandir}/man1/radeontop.1*


%changelog
* Mon Jul 13 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.8-2.git20150215.281462c
- Drop the Group
- Fix a spelling mistake
- Fix recompilation
- Use license for COPYING

* Sun Feb 15 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.8-1.git20150215.281462c
- Update to upstream 0.8

* Thu Apr 24 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-2.git20140421.eadc100
- Fix commit position, BuildRequirements, build, and man page inclusion (thanks mschwendt)

* Mon Apr 21 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-1.git20140421.eadc100
- Initial package
