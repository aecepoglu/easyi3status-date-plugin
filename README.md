easyi3status date plugin
------------------------

Demo: `16-09-2017 15:46`

## To install

    wget https://raw.githubusercontent.com/aecepoglu/easyi3status-date-plugin/master/date.py -P ~/.config/easyi3status/modules/
    wget https://raw.githubusercontent.com/aecepoglu/easyi3status-date-plugin/master/config.yaml -O - >> ~/.config/easyi3status/config.yaml
    #and *restart* i3

### Or do these manually:

Copy `date.py` to `~/.config/easyi3status/modules/`
Add its configuration to your `config.yaml`

## Configuration

Add these under `modules` in `~/.config/easyi3status/config.yaml`

    - name: date
      config:
        format: '%H:%M'


* `format`: date format. See [this page](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) for its documentation. Optional. Defaults to `'%d-%m-%Y %H:%M'`
