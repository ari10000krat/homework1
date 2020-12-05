def parse_parameters(query: str) -> dict:
	"""
        The function parses parameters from a string
        :param request:  request string
        :return: parameters
    """
    dict_parametrs = {}
    requestindex = request.find('?')
    if len(request[requestindex:]) != 1:
        request = request[requestindex + 1:]
        arr_parametrs = [s.split('=') for s in request.split('&')]
        dict_parametrs = {s[0]: s[1] for s in arr_parametrs}
    return dict_parametrs


def parse_cookies(query: str) -> dict:
    return {}


if __name__ == '__main__':

    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
        assert parse_parameters('https://mail.google.com/mail/u/0/?tab=rm') == {'tab': 'rm'}
    assert parse_parameters(
        'https://www.google.com/search?q=telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D1%8B&oq=telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB&aqs=chrome.0.0i433j69i57j0l6.9788j0j7&sourceid=chrome&ie=UTF-8') == \
           {'q': 'telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB%D1%8B',
            'oq': 'telegram+%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB',
            'aqs': 'chrome.0.0i433j69i57j0l6.9788j0j7',
            'sourceid': 'chrome',
            'ie': 'UTF-8'}
    assert parse_parameters(
        'https://rozetka.com.ua/?gclid=CjwKCAjw0On8BRAgEiwAincsHPoy20JoXn1-U8KFRsx3JH9siOtxoXQsWIel6KvI4MU9chAipecK6RoCO0EQAvD_BwE') == \
           {'gclid': 'CjwKCAjw0On8BRAgEiwAincsHPoy20JoXn1-U8KFRsx3JH9siOtxoXQsWIel6KvI4MU9chAipecK6RoCO0EQAvD_BwE'}
    assert parse_parameters('https://www.youtube.com/watch?v=o3zIjodedhA&ab_channel=XYZ') == {'v': 'o3zIjodedhA',
                                                                                              'ab_channel': 'XYZ'}
    assert parse_parameters('https://www.youtube.com/watch?v=XwpHbbXZvXA&ab_channel=ZProger%5BIT%5D') == {
        'v': 'XwpHbbXZvXA',
        'ab_channel': 'ZProger%5BIT%5D'}
    assert parse_parameters('https://www.youtube.com/watch?v=0oBi8OmjLIg&ab_channel=JomaTech') == {'v': '0oBi8OmjLIg',
                                                                                                   'ab_channel': 'JomaTech'}
    assert parse_parameters('https://www.youtube.com/watch?v=XZmGGAbHqa0&ab_channel=GoogleWorkspace') == {
        'v': 'XZmGGAbHqa0',
        'ab_channel': 'GoogleWorkspace'}
    assert parse_parameters('https://www.youtube.com/watch?v=ZBimwHa2FPY&ab_channel=WebForMySelf') == {
        'v': 'ZBimwHa2FPY',
        'ab_channel': 'WebForMySelf'}


    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=GLEB;') == {'name': 'GLEB'}
    assert parse_cookies('name=Dima;color=red;') == {'name': 'Dima',
                                                     'color': 'red'}
    assert parse_cookies('value=123;name=GLEB;') == {'value': '123',
                                           'name': 'GLEB'}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('domain=cit-forum.com;') == {'domain': 'cit-forum.com'}
    assert parse_cookies('path=PATH;Content-type=text\html;') == {'path': 'PATH',
                                                                 'Content-type': 'text\html'}
    assert parse_cookies('expires=Wednesday, 09-Nov-99 23:12:40 GMT;') == {
        'expires': 'Wednesday, 09-Nov-99 23:12:40 GMT'}
    assert parse_cookies('DOMAIN=domain_name;') == {'DOMAIN': 'domain_name'}
    assert parse_cookies('tasty_cookie=strawberry;') == {'tasty_cookie': 'strawberry'}
