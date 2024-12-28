import { createClient } from '@supabase/supabase-js';

// Supabase credentials
const SUPABASE_URL = 'https://xchoumvoqnkgpywmiiqg.supabase.co';
const SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhjaG91bXZvcW5rZ3B5d21paXFnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzUxNjg5ODUsImV4cCI6MjA1MDc0NDk4NX0.-kbMao3J8LIal337g_FW2954chEm3kVXXAGaNf3AriY';

export const supabase = createClient(SUPABASE_URL, SUPABASE_API_KEY);

// Function to fetch invoices from the 'invoices' table
export const fetchInvoices = async () => {
    const { data, error } = await supabase.from('invoices').select('*');
    if (error) {
        console.error('Error fetching invoices:', error.message);
        throw new Error(error.message);
    }
    return data;
};

// Add other utility functions as needed
