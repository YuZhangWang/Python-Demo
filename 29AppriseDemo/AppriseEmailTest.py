from shlex import quote

import apprise


def notify_myself(email: str, sckey: str, secure: bool = True, auto_send: bool = True):
    """
    使用自己的邮箱给自己发送邮件。

    ## POP3/SMTP 链接

    - QQ
        https://mail.qq.com/cgi-bin/frame_html?sid=x55BO9EFSFO6TlIz&r=990fe85bc8c2689efad083981d51b433
    - 163
        https://mail.163.com/js6/main.jsp?sid=zCQizbVqESZFlceTcxqqacMvYKCkOqZW&df=mail163_letter#
        module=options.LinkModule%7C%7B%22link%22%3A%22option_pop3%22%7D

    :param email: 邮箱账号，如 `awesome@gmail.com`
    :param sckey: 授权码，前往后台，开启 `POP3/SMTP服务`
    :param secure: 开启所谓的 `安全连接`
    :param auto_send: 自动发送邮件
    :return:
    """
    # 处理关键字映射
    _email_id = quote(email.split("@")[0])
    _email_domain = quote(email.split("@")[-1])
    _sckey = quote(sckey)

    _smtp_mapping = {
        "163.com": "smtp.163.com",
        "qq.com": "smtp.qq.com",
    }

    # secure: "mailtos://163.com?smtp=smtp.163.com&user={}&pass={}&mode=ssl"
    # standard: "mailto://163.com?smtp=smtp.163.com&user={}&pass={}"
    url_template = f"{_email_domain}?smtp={_smtp_mapping[_email_domain]}" \
                   f"&user={_email_id}" \
                   f"&pass={_sckey}"

    if secure:
        url_template = f"mailtos://{url_template}&mode=ssl"
    else:
        url_template = f"mailto://{url_template}"

    print(url_template)

    # 发送推送
    if auto_send:
        surprise = apprise.Apprise()

        surprise.add(url_template)

        surprise.notify(
            body='what a great notification service!',
            title='NotifyMyself secure:{}'.format(secure),
        )
        
        
if __name__ == '__main__':
    notify_myself("YuZhangWang233@163.com", "", secure=False)
    
