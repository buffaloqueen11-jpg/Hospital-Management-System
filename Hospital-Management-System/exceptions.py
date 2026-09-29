class HospitalError(Exception):
    """Base exception for Hospital Management System."""
    pass


class PatientNotFoundError(HospitalError):
    """Raised when a patient is not found."""
    pass


class DoctorNotFoundError(HospitalError):
    """Raised when a doctor is not found."""
    pass


class AppointmentNotFoundError(HospitalError):
    """Raised when an appointment is not found."""
    pass

class MedicalRecordNotFoundError(HospitalError):

    """Raised when a medical record is not found."""

    pass

class PrescriptionNotFoundError(HospitalError):
    """Raised when a prescription is not found."""
    pass

class PaymentNotFoundError(HospitalError):
    """Raised when a payment is not found."""
    pass