import PatientClass as patient
import ProcedureClass as procedure

def main():

    patient1 = patient.Patient(1, 'Matt Jones', '123 Main St, Waco, TX 76706', '254-555-7415', True)

    physical = procedure.Procedure('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1)
    mri = procedure.Procedure('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1)
    ct_scan = procedure.Procedure('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2)

    patients = [patient1]
    procedures = [physical, mri, ct_scan]

    for pat in patients:
        total_bill = 0
        print('\n*** Patient Bill ***')
        print('Name:', pat.get_name())
        print('Address:', pat.get_address())
        print('Phone:', pat.get_phone())
        for proc in procedures:
            if pat.get_patient_id() == proc.get_patient_id():
                print('\nProcedure:', proc.get_procedure_name())
                print('Date:', proc.get_date())
                print('Charge: $', format(proc.get_charge(), '.2f'), sep = '')
                
                total_bill += proc.get_charge()
        
        if pat.get_veteran_status():
            total_bill *= .6

        print('\nTotal Charges: $', format(total_bill, '.2f'), '\n', sep = '')

main()
