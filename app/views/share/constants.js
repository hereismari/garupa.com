app.constant('Day', {
    SUN: 'dom',
    MON: 'seg',
    TUE: 'ter',
    WED: 'qua',
    THU: 'qui',
    FRI: 'sex',
    SAT: 'sab'
});

app.constant('Way', {
    TO: 0,
    FROM: 1
});

app.constant('ModalMessage', {
	SEND_INVITATION : { title: 'Enviar solicitacao de carona', message: 'O usuario sera notificado que voce quer essa carona!'},
	NOTIFY_ME : { title: 'Quero ser notificado', message: 'Voce sera notificado assim que uma carona desse tipo surgir!'},
	MAKE_A_FRIEND : { title: 'Solicitacao de amizade', message: 'O usuario sera notificado que voce quer ser seu amigo!'}
});
