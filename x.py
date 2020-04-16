def get_points(self, captcha_result):
    """
    解析识别结果
    :param captcha_result: 识别结果
    :return: 转化后的结果
    """
    groups = captcha_result.get('pic_str').split('|')
    locations = [[int(number) for number in group.split(',')] for group in groups]
    return locations


def touch_click_words(self, locations):
    """
    点击验证图片
    :param locations: 点击位置
    :return: None
    """
    for location in locations:
        ActionChains(self.browser).move_to_element_with_offset(self.get_captcha_element(), location[0],
                                                               location[1]).click().perform()
        time.sleep(1)