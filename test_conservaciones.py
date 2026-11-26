import pytest
import Conversiones as con

def test_pulgadas_cm():
    assert con.centimetrosApulgadas(5.08) == pytest.approx(2)
    assert con.pulgadasAcentimetros(2) == pytest.approx(5.08)

def test_millas_km():
    assert con.kilometrosAmillas(3.218688) == pytest.approx(2)
    assert con.millasAkilometros(2) == pytest.approx(3.218688)
