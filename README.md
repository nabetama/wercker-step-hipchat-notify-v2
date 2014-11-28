# hipchat-notify

Send a message to a HipChat room.
This is using the [HipChat API V2](https://www.hipchat.com/docs/apiv2) and
can specify the target branch to notify.
.

# What's new

- released 0.0.62.

# Options

* `token` (required) Your HipChat token(API V2).
* `room-id` (required) The id of the HipChat room. (retrieve yours from https://www.hipchat.com/rooms/ids)
* `passed-message` (optional) The message which will be shown on a passed build or deploy.
* `failed-message` (optional) The message which will be shown on a failed build or deploy.
* `passed-color` (optional, default: `green`) The color of a passed build/deploy message in HipChat.
* `failed-color` (optional, default: `red`) The color of a failed build/deploy message in HipChat.
* `passed-notify` (optional, default: `false`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `failed-notify` (optional, default: `true`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `from-name` (optional, default: `wercker`) Use this option to override the name that will appear in the room as sender.
* `on` (optional, default: `always`) When should this step send a message. Possible values: `always` and `failed`.
* `target-branch` (optional, default: `all`) The branch of a notify target.

# Example

Add HIPCHAT_TOKEN as deploy target or application environment variable.


### wercker.yml in your application.

```yaml
build:
  steps:
    - script:
      name: 'pip install hypchat'
      sudo: yes
      code: |
        pip install hypchat
  after-steps:
    - hipchat-notify:
      token: $HIPCHAT_TOKEN
      room-id: id
      from-name: name
      target-branch: master
```

# License

The MIT License (MIT)

# Changelog

## 0.0.62
- This application is dependent on [hypchat](https://github.com/RidersDiscountCom/HypChat).

# wercker status

