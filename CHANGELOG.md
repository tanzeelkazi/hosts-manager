# Change Log

## 1.3.0 (May 16, 2017)

 - Update readme to specify semver spec version (2.0.0).
 - Update ahe (Apache Hosts Export) to read `ServerAlias`
   directive.
 - Add SVG logo for `hm`.
 - The script now takes the original user's username even
   when run under the `sudo` context.
 - The version of the script used to generate the output is
   now printed in the hosts file.


## 1.2.1 (May 12, 2017)

 - Add note about semantic versioning in readme.
 - Update indentation of all list items to have consistent
   behavior across standard markdown viewers.


## 1.2.0 (May 12, 2017)

 - Add support for nested hosts configurations
 - Add more verbose hosts-file comments in the output
 - Sort methods by name
 - Remove recommendation to symlink to `/usr/local/bin` since
   the script is to support configurations from multiple users.
 - Updated all the readme files to reflect the new nested-config option.


## 1.1.0 (May 8, 2017)

 - Update README for the package to include an index
 - Update README for plugins to add an index
   and add an uninstall section.
 - Now the `Apache Hosts Export` plugin uses the same
   version as the `Hosts Manager` package. This was done
   because the plugin is available out-of-the-box as part
   of the package any way, so it doesn't make sense to
   maintain two semvers.


## 1.0.0 (May 7, 2017)

 - Initial release
