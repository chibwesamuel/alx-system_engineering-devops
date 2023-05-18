# Tests how well the server works under pressure

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['nginx-restart'], # Trigger Nginx restart after modifying the file
}

# Restart Nginx
exec { 'nginx-restart':
  command     => 'nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true, # Only run this command when triggered by the 'fix--for-nginx' exec
}

# Notify the user about the requirement to check the logs
notify { 'Check Nginx logs for troubleshooting':
  message => 'Review Nginx logs to identify and address any potential issues.',
}
