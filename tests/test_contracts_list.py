# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, CloudBlue
# All rights reserved.
#

from reports.contract_list.entrypoint import generate


def test_generate(progress, client_factory, response_factory, contract_response):
    responses = []

    parameters = {
        "type": None,
        "status": None,
    }
    responses.append(
        response_factory(
            count=1
        )
    )

    responses.append(
        response_factory(
            value=[contract_response]
        )
    )

    client = client_factory(responses)

    result = list(generate(client, parameters, progress))

    assert len(result) == 1
    for res in result:
        assert res != "-"
        assert res is not None


def test_generate_all_params(progress, client_factory, response_factory, contract_response):
    responses = []

    parameters = {
        "type": ['distribution'],
        "status": ["active"]
    }
    responses.append(
        response_factory(
            count=1
        )
    )

    responses.append(
        response_factory(
            query='and(in(type,(distribution)),in(status,(active)))',
            value=[contract_response]
        )
    )

    client = client_factory(responses)

    result = list(generate(client, parameters, progress))

    assert len(result) == 1
    for res in result:
        assert res != "-"
        assert res is not None
