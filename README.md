# SSSD GDB Extensions

Set of extensions that will help you debug SSSD in GDB.

## Usage

Put the following line in your (`~/.gdbinit`) or run the command
directly from gdb. Replace `$repo` with path to the cloned repository.

```
source $repo/sssd_gdb/load.py
```

## Capabilities

### Pretty Printers

There are pretty printers available for:

* `ldb` structures (from `ldb_result` to `ldb_val`)

## Examples

### Pretty Print ldb_result

```gdb
(gdb) p *result->ldb_result
$1 = messages: 3
  dn: unsupported, elements: 11
    flags: 0, name: 0xd20a20 "gecos", values: 1
      len: 7 0xd20e10 "vagrant"

    flags: 0, name: 0xd08320 "gidNumber", values: 1
      len: 6 0xd20e80 "100100"

    flags: 0, name: 0xd15990 "name", values: 1
      len: 13 0xd21910 "vagrant@ad.vm"

    flags: 0, name: 0xd1dd70 "objectCategory", values: 1
      len: 4 0xd15a00 "user"

    flags: 0, name: 0xd147d0 "uidNumber", values: 1
      len: 6 0xd07f10 "100100"

    flags: 0, name: 0xd207d0 "objectSIDString", values: 1
      len: 45 0xd16140 "S-1-5-21-433998187-2822908608-1404606238-1000"

    flags: 0, name: 0xd161e0 "uniqueID", values: 1
      len: 36 0xd167c0 "54a342d3-2653-49f8-906e-9f942ffdf4c4"

    flags: 0, name: 0xd177d0 "originalDN", values: 1
      len: 31 0xd0a770 "CN=vagrant,CN=Users,DC=ad,DC=vm"

    flags: 0, name: 0xd20210 "lastUpdate", values: 1
      len: 10 0xd07ac0 "1594819355"

    flags: 0, name: 0xd23100 "dataExpireTimestamp", values: 1
      len: 10 0xd14a00 "1594824755"

    flags: 0, name: 0xd23280 "initgrExpireTimestamp", values: 1
      len: 10 0xd22910 "1594824756"

  dn: unsupported, elements: 8
    flags: 0, name: 0xd1d120 "gidNumber", values: 1
      len: 1 0xd1d220 "0"

    flags: 0, name: 0xd1d290 "name", values: 1
      len: 15 0xd1d380 "non-posix@ad.vm"

    flags: 0, name: 0xd1d400 "objectCategory", values: 1
      len: 5 0xd1d500 "group"

    flags: 0, name: 0xd1d570 "lastUpdate", values: 1
      len: 10 0xd238b0 "1594819355"

    flags: 0, name: 0xd23930 "dataExpireTimestamp", values: 1
      len: 10 0xd23a30 "1594819354"

    flags: 0, name: 0xd23ab0 "isPosix", values: 1
      len: 5 0xd23ba0 "FALSE"

    flags: 0, name: 0xd23c10 "originalDN", values: 1
      len: 33 0xd0b380 "CN=non-posix,CN=Users,DC=ad,DC=vm"

    flags: 0, name: 0xd23d10 "objectSIDString", values: 1
      len: 45 0xd23e10 "S-1-5-21-433998187-2822908608-1404606238-1107"

  dn: unsupported, elements: 8
    flags: 0, name: 0xd1a530 "gidNumber", values: 1
      len: 1 0xd248f0 "0"

    flags: 0, name: 0xd24960 "name", values: 1
      len: 18 0xd24a50 "Domain Users@ad.vm"

    flags: 0, name: 0xd24ad0 "objectCategory", values: 1
      len: 5 0xd24bd0 "group"

    flags: 0, name: 0xd24c40 "lastUpdate", values: 1
      len: 10 0xd24d40 "1594819356"

    flags: 0, name: 0xd24dc0 "dataExpireTimestamp", values: 1
      len: 10 0xd24ec0 "1594819355"

    flags: 0, name: 0xd24f40 "isPosix", values: 1
      len: 5 0xd25030 "FALSE"

    flags: 0, name: 0xd250a0 "originalDN", values: 1
      len: 36 0xd14f30 "CN=Domain Users,CN=Users,DC=ad,DC=vm"

    flags: 0, name: 0xd251a0 "objectSIDString", values: 1
      len: 44 0xd252a0 "S-1-5-21-433998187-2822908608-1404606238-513"
(gdb)
```