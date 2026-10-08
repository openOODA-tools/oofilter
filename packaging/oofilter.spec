Name:           oofilter
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign boolean logic evaluator and stream predicate filter in pure openOODA.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/oofilter
Source0:        oofilter-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oofilter is a sovereign boolean logic evaluator and stream predicate filter
written in pure openOODA, featuring zero ambient authority, field indexing,
relational comparisons, and a streaming MCP JSON-RPC 2.0 stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oofilter
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oofilter-uninstall

%files
/usr/bin/oofilter
/usr/bin/oofilter-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevation to v0.2.0 with boolean predicate AST, field selectors, and streaming MCP
