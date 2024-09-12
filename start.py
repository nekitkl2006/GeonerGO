from Naked.toolshed.shell import muterun_js


# второй параметр -- адрес кошелька пользователя, который запрашиваем дивиденты
response = muterun_js('dist/app.js', 'EQA3my3Wj6yTn1NY2AnDWS1eVZ_zVqSX9rEUGTVWoNaEbxfP')
print(response.stderr)
if response.exitcode == 0:
    # the command was successful, handle the standard output
    standard_out = response.stdout
    print(standard_out)
else:
    # the command failed or the executable was not present, handle the standard error
    standard_err = response.stderr
    exit_code = response.exitcode
    print(type(standard_err))
    print('Exit Status ' + str(exit_code) + ': ' + standard_err.decode('unicode_escape'))