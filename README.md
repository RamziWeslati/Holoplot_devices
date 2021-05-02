# Holoplot_devices
This repo holds a both client/server code for Holoplot sound devices

# Usage

## Configure server or use default config
Multipliers can be configured in `device_server/app/config.py`

1. You can change the role assigned to a multiplier by changing the key of the `ROLES_BY_MULTIPLIER` dictionary
```python
    ROLES_BY_MULTIPLIER = {
        3: 'NewBing',
        5: 'NewBang',
    }
```
2. You can add another role by adding an item to the `ROLES_BY_MULTIPLIER` dictionary
```python
    ROLES_BY_MULTIPLIER = {
        3: 'Bing',
        5: 'Bang',
        7: 'KaBoom'
    }
```
using this config, a device with the id: `14` would have the role `KaBoom`. 
While a device with role `21` will have the role `Meh` ( because 21 is not a multiple of 3 ).
And a device with the id `105` will have the role defaulted to `Boom` as `3 x 5 x 7 = 105`

3. you can change the values of  ```ROLE_ALL_MULTIPLIERS``` and ```ROLE_NONE_MULTIPLIERS```
which are defaulted to ```Boom``` and ```Meh``` respectfully, by changing their values in the `BaseConfig` class in `device_server/app/config.py`

## run server     
```bash
export FLASK_ENV=app
export FLASK_APP=device_server/app
pip install -r device_server/requirements.txt
python -m flask run
```

## run server unit tests
```bash
python3 -m pytest ./device_server
```

## run client
```bash
go run ./client/ <device_id>
```

# Who you gonna call ![Ghostbusters](https://i.ibb.co/J3WD1ct/Webp-net-resizeimage.png)

Ramzi Oueslati, Junior software engineer, [email](mailto:ramzi.oueslati@ensi-uma.tn)

