#!/usr/bin/env bash
# puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    # SSH client configuration
    Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
}

